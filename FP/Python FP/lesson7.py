def ConquestCampaign(N, M, L, battalion):
    captured = set()
    for i in range(0, len(battalion), 2):
        captured.add((battalion[i], battalion[i + 1]))
  
    def simulate_day(day, current_captured, total_areas):
        if len(current_captured) == total_areas:
            return day
        new_captured = set()
        for x, y in current_captured:
            neighbors = list(filter(
                lambda pos: 1 <= pos[0] <= N and 1 <= pos[1] <= M,
                [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            ))
            new_captured.update(neighbors)
        all_captured = current_captured.union(new_captured)
        return simulate_day(day + 1, all_captured, total_areas)

    return simulate_day(1, captured, N * M)
