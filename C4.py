def loaded_divider(vs, r1, r2, rl):

    r2_parallel_rl = (r2 * rl) / (r2 + rl)

    v_unloaded = vs * (r2 / (r1 + r2))

    v_loaded = vs * (r2_parallel_rl / (r1 + r2_parallel_rl))
    
    return (v_unloaded, v_loaded)

unloaded, loaded = loaded_divider(12, 1000, 1000, 500)
print(f"loaded_divider(12, 1000, 1000, 500) -> ({unloaded:.1f}, {loaded:.1f})")
