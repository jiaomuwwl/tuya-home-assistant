#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Config flow for Tuya."""

import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers import config_entry_oauth2_flow

from .const import (
    CONF_COUNTRY_CODE,
    DOMAIN,
    CONF_ENDPOINT,
    CONF_ACCESS_ID,
    CONF_ACCESS_SECRET,
    CONF_USERNAME,
    CONF_PASSWORD,
    CONF_PROJECT_TYPE,
    TUYA_ENDPOINT,
    TUYA_PROJECT_TYPE
)

from tuya_iot import TuyaOpenAPI, ProjectType

RESULT_SINGLE_INSTANCE = "single_instance_allowed"

_LOGGER = logging.getLogger(__name__)

## Project Type 
DATA_SCHEMA_PROJECT_TYPE = vol.Schema(
    {
        vol.Required(CONF_PROJECT_TYPE): vol.In(TUYA_PROJECT_TYPE)
    }
)

## INDUSTY_SOLUTIONS Schema
DATA_SCHEMA_INDUSTY_SOLUTIONS = vol.Schema(
    {     
        vol.Required(CONF_ENDPOINT): vol.In(TUYA_ENDPOINT),
        vol.Required(CONF_ACCESS_ID): str,
        vol.Required(CONF_ACCESS_SECRET): str,
        vol.Required(CONF_USERNAME): str,
        vol.Required(CONF_PASSWORD): str,
    }
)

## SMART_HOME Schema
DATA_SCHEMA_SMART_HOME = vol.Schema(
    {     
        vol.Required(CONF_ENDPOINT): vol.In(TUYA_ENDPOINT),
        vol.Required(CONF_COUNTRY_CODE): str,
        vol.Required(CONF_ACCESS_ID): str,
        vol.Required(CONF_ACCESS_SECRET): str,
        vol.Required(CONF_USERNAME): str,
        vol.Required(CONF_PASSWORD): str,
    }
)


# @config_entries.HANDLERS.register(DOMAIN)
# class TuyaFlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler):
#     """Config flow to handle Tuya OAuth2 authentication."""

#     DOMAIN = DOMAIN
#     CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

#     @property
#     def logger(self) -> logging.Logger:
#         """Return logger."""
#         return logging.getLogger(__name__)

#     async def async_step_user(self, user_input=None):
#         """Handle a flow start."""
#         if self.hass.config_entries.async_entries(DOMAIN):
#             return self.async_abort(reason="single_instance_allowed")

#         return await super().async_step_user(user_input)

class TuyaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    conf_project_type = None

    def _try_login(self, user_input):
        print('TuyaConfigFlow._try_login start, user_input:', user_input)
        project_type = ProjectType(user_input[CONF_PROJECT_TYPE])
        api = TuyaOpenAPI(user_input[CONF_ENDPOINT], user_input[CONF_ACCESS_ID], user_input[CONF_ACCESS_SECRET], project_type)
        api.set_dev_channel('hass')

        response = api.login(user_input[CONF_USERNAME], user_input[CONF_PASSWORD]) if project_type == ProjectType.INDUSTY_SOLUTIONS else\
             api.login(user_input[CONF_USERNAME], user_input[CONF_PASSWORD], user_input[CONF_COUNTRY_CODE])

        print('TuyaConfigFlow._try_login finish, response:', response)
        return response

    async def async_step_import(self, user_input=None):
        return await self.async_step_user(user_input, is_import=True)

    async def async_step_project_type(self, user_input=None):
        self.conf_project_type = user_input[CONF_PROJECT_TYPE]
        self.project_type = ProjectType(self.conf_project_type)
        return self.async_show_form(
            step_id='user',
            data_schema=DATA_SCHEMA_SMART_HOME
        ) if self.project_type == ProjectType.SMART_HOME else self.async_show_form(
            step_id='user',
            data_schema=DATA_SCHEMA_INDUSTY_SOLUTIONS
        )

    async def async_step_user(self, user_input=None, is_import=False):
        print('TuyaConfigFlow.async_step_user start, is_import=', user_input)
        
        if self._async_current_entries():
            return self.async_abort(reason=RESULT_SINGLE_INSTANCE)

        errors = {}
        if user_input is not None:
            if self.conf_project_type is not None:
                user_input[CONF_PROJECT_TYPE] = self.conf_project_type

            response = await self.hass.async_add_executor_job(self._try_login, user_input)

            if response.get('success', False):
                print('TuyaConfigFlow.async_step_user login success')
                return self.async_create_entry(
                    title=user_input[CONF_ACCESS_ID],
                    data=user_input,
                )
            else:
                errors['base'] = 'code={}, msg={}'.format(response.get('code', 0), response.get('msg', ''))
                if is_import == True:
                    return self.async_abort(reason=errors['base'])
        
        return self.async_show_form(
            step_id='project_type',
            data_schema=DATA_SCHEMA_PROJECT_TYPE,
            errors=errors
        )

