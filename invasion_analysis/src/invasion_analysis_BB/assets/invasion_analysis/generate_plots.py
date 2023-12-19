import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sb
import sys


def process_parameters():
    if len(sys.argv) < 2:
        print("Please specify name for the output")
        sys.exit(1)

    parameters_file = sys.argv[1]
    plots_directory = sys.argv[2]
    simulations_paths = sys.argv[3:]

    print("Generating plots....")
    print("- parameters set : %s" % parameters_file)
    print("- plots directory : %s" % plots_directory)
    print("- simulations path : %s" % simulations_paths)

    return parameters_file, plots_directory, simulations_paths


def sigmoid(x, y0, ymax, k, x0):
    y = y0 + ymax / (1 + np.exp(-k * (x - x0)))
    return y


def main(parameters_file, plots_directory, simulations_paths):
    parameters_sets = []
    with open(parameters_file, "r") as psets:
        for line in psets.readlines():
            # print(line)
            raw_pset = line.split(",")
            # print(raw_pset)
            for value in raw_pset[1:]:
                parameters_sets.append((raw_pset[0].strip(), float(value.strip())))

    parameters_data = {}

    for i_set, parameter_set in enumerate(parameters_sets):
        parameter, value = parameter_set
        data_file = simulations_paths[
            i_set
        ]  # TODO: must be double checked? (they are in the same order)
        df = pd.read_csv(data_file)
        values = df.iloc[-1]
        if parameter not in parameters_data.keys():
            parameters_data[parameter] = {value: values}
        else:
            parameters_data[parameter].update({value: values})

    for parameter in parameters_data.keys():
        df = pd.DataFrame(parameters_data[parameter])

        fig, ax = plt.subplots(1, figsize=(5, 3), dpi=500, tight_layout=True)

        fields = ["single", "cells_in_cluster"]  # , 'ratio']
        for i, field in enumerate(fields):
            # ax.errorbar(df.columns, df.loc[field, :], df.loc['error_%s' % field],fmt='.', label=field)
            ax.errorbar(
                df.columns,
                df.loc[field, :],
                df.loc["error_%s" % field],
                alpha=0.75,
                fmt=":",
                capsize=3,
                capthick=1,
                label=field,
                color="C%d" % i,
            )
            data = {
                "x": df.columns,
                "y1": [
                    y - e for y, e in zip(df.loc[field, :], df.loc["error_%s" % field])
                ],
                "y2": [
                    y + e for y, e in zip(df.loc[field, :], df.loc["error_%s" % field])
                ],
            }
            plt.fill_between(**data, alpha=0.25, label="_nolegend_", color="C%d" % i)

            from scipy.optimize import curve_fit

            popt, pcov = curve_fit(
                sigmoid,
                df.columns,
                df.loc[field, :],
                p0=[df.loc[field, 0], df.loc[field, :].iloc[-1], 1, 1],
                maxfev=1000000000,
            )

            yfit = [sigmoid(xdatum, *popt) for xdatum in df.columns]
            ax.plot(df.columns, yfit, color="C%d" % i)
        plt.xlabel("%s value" % parameter)
        plt.ylabel("population size (cells)")
            
        fig.legend()
        try:
            os.makedirs(plots_directory)
        except FileExistsError:
            # directory already exists
            pass
        fig.savefig(os.path.join(plots_directory, "%s.png" % parameter))

        fig, ax = plt.subplots(1, figsize=(5, 3), dpi=500, tight_layout=True)

        field = "ratio"
        ax.errorbar(
            df.columns,
            df.loc[field, :],
            df.loc["error_%s" % field],
            alpha=0.75,
            fmt=":",
            capsize=3,
            capthick=1,
            label=field,
            color="C0",
        )
        data = {
            "x": df.columns,
            "y1": [y - e for y, e in zip(df.loc[field, :], df.loc["error_%s" % field])],
            "y2": [y + e for y, e in zip(df.loc[field, :], df.loc["error_%s" % field])],
        }
        plt.fill_between(**data, alpha=0.25, label="_nolegend_", color="C0")

        from scipy.optimize import curve_fit

        popt, pcov = curve_fit(
            sigmoid,
            df.columns,
            df.loc[field, :],
            p0=[df.loc[field, 0], df.loc[field, :].iloc[-1], 1, 1],
            maxfev=1000000000,
        )

        yfit = [sigmoid(xdatum, *popt) for xdatum in df.columns]
        ax.plot(df.columns, yfit, color="C0")
        plt.xlabel("%s value" % parameter)
        plt.ylabel("collective migration (% of cells)")
        fig.legend()
        fig.savefig(os.path.join(plots_directory, "%s_ratio.png" % parameter))
    print("Done")


if __name__ == "__main__":
    parameters_file, plots_directory, simulations_paths = process_parameters()
    main(parameters_file, plots_directory, simulations_paths)
