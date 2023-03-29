using COBREXA, Tulip

m = load_model(ARGS[1])

f = open(ARGS[2], "w")
rs = reactions(m)
for i in rs
    println(f, i)
end
