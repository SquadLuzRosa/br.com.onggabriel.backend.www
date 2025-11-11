from decouple import config


class EnvUtils:
    """
    Utilities for handling environment variables.
    Provides methods to convert environment variable values to appropriate types.
    """

    @staticmethod
    def env_str_to_boolean(env_var_name: str) -> bool:
        """
        Converts the value of an environment variable to boolean.
        The variable name is always treated as uppercase.
        Accepts: 'true', '1', 'yes' (case-insensitive) as True.
        Accepts: 'false', '0', 'no' (case-insensitive) as False.
        Raises ValueError for invalid values or if variable is not set.

        Args:
            env_var_name (str): The name of the environment variable.
        Returns:
            bool: The converted boolean value.
        """
        env_var_name = env_var_name.upper()

        value = config(env_var_name, None)
        if value is None:
            raise ValueError(f"Environment variable '{env_var_name}' is not set.")

        true_values = {'true', '1', 'yes'}
        false_values = {'false', '0', 'no'}

        value = str(value).lower()
        value_str = str(value) if not isinstance(value, str) else value
        value_lower = value_str.lower()

        if value_lower in true_values:
            return True
        elif value_lower in false_values:
            return False
        else:
            raise ValueError(
                f'Invalid value for boolean conversion: "{value_str}" '
                f'in variable "{env_var_name}"'
            )
