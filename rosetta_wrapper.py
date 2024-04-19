# rosetta_wrapper.py


def process_data_with_rosetta(df, vars, v=3, conf=None, include_sd=False):
    """
    Parameters:
    - df (DataFrame): The the DataFrame to be processed.
    - vars (list): List of variable names to be processed.
    - v (str): The version of the ROSETTA model to use.
    - conf (dict, optional): Additional request configuration options.
    - include_sd (bool): Whether to include standard deviation in the output.

    Returns:
    - DataFrame: The processed results from the ROSETTA python package.
    """
    # Select only the specified vars columns and other columns
    df_vars = df[vars]
    df_other = df.drop(columns=vars)

    # Convert the vars df to a matrix (2D list)
    df_vars_matrix = df_vars.values.tolist()

    mean, stdev, codes = rosetta(v, SoilData.from_array(df_vars_matrix))

    # Convert van Genuchten params to DataFrame
    vg_params = pd.DataFrame(mean)
    vg_params.columns = ["theta_r", "theta_s", "alpha", "npar", "ksat"]

    # Add model codes and version to the DataFrame
    vg_params[".rosetta.model"] = pd.Categorical.from_codes(
        codes, categories=["-1", "1", "2", "3", "4", "5"]
    )
    vg_params[".rosetta.version"] = v

    # If include_sd is True, add standard deviations to the DataFrame
    if include_sd:
        vg_sd = pd.DataFrame(stdev)
        vg_sd.columns = [f"sd_{name}" for name in vg_params.columns]
        result = pd.concat(
            [
                df_other.reset_index(drop=True),
                df_vars.reset_index(drop=True),
                vg_params.reset_index(drop=True),
                vg_sd,
            ],
            axis=1,
        )
    else:
        result = pd.concat(
            [
                df_other.reset_index(drop=True),
                df_vars.reset_index(drop=True),
                vg_params.reset_index(drop=True),
            ],
            axis=1,
        )

    return result
