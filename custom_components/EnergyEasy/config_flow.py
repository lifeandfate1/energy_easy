async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
    """Invoked when a user initiates a flow via the user interface."""
    errors: Dict[str, str] = {}
    if user_input is not None:
        try:
            await validate_auth(user_input[CONF_ACCESS_TOKEN], self.hass)
        except ValueError:
            errors["base"] = "auth"
        if not errors:
            # Input is valid, set data.
            self.data = user_input
            self.data[CONF_REPOS] = []
            # Return the form of the next step.
            return await self.async_step_repo()

    return self.async_show_form(
        step_id="user", data_schema=AUTH_SCHEMA, errors=errors
    )
