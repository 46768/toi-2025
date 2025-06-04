# Prints longest cycle
print(list(reversed(sorted([
    # Get size of each cycles
    len(x) for x in (lambda y,u:(
        # Get all cycles
        lambda v:[
            # Cycle detector lambda (returns nodes in cycle that have input node)
            (lambda t,s,ss:[(r,s.append(v[r]),ss.add(r),y.add(r))[0]for r in s if r not in ss])
            # Apply each node to detector if not in global visited (y)
            # (node, comp iterator, node in cycle)
            (z,[z],set()) for z in range(u) if (z not in y)])
                    # Input formatting ({node_src: node_dest})
                    ({i:int(input())-1 for i in range(u)}))
    # (Global visited set, node count input)
    (set(),int(input()))])))
      # Get the longest cycle
      [0])
