
#  Redo 2026-11-14: re-solved from scratch, same set approach.
#  Mistakes hit (again): built seen from the range instead of from nums (seen.add(x) then
#  `x not in seen` is always False); range(1, len(nums)) skipped n -> range(1, len(nums) + 1).
