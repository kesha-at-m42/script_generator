extends SequenceEvent

func trigger() -> void:
	var frac_bar := get_frac_shape()
	reset_cuts(frac_bar)
	await delay(1)
	use_cut_tool(frac_bar, 1, 2)
	await delay(1)
	use_cut_tool(frac_bar, 1, 4)
	await delay(1)
	use_cut_tool(frac_bar, 3, 4)
