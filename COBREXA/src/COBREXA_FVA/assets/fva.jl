using COBREXA, Tulip

m = load_model(ARGS[1])

res = flux_variability_analysis(m, Tulip.Optimizer; bounds = objective_bounds(0.99))

open(ARGS[2], "w") do f
    println(f, "reaction\tminimum\tmaximum")
    for (r, (rmin, rmax)) in zip(reactions(m), eachrow(res))
        println(f, "$r\t$rmin\t$rmax")
    end
end
