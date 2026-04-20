extends SequenceEvent

func trigger() -> void:
	var frac_bar = get_frac_shape()
	reset_cuts(frac_bar)
	await delay(0.5)
	use_cut_tool(frac_bar, 1, 2)
	await delay(1)
	use_cut_tool(frac_bar, 1, 6)
	await delay(0.25)
	use_cut_tool(frac_bar, 2, 6)
	await delay(1)
	use_cut_tool(frac_bar, 4, 6)
	await delay(0.25)
	use_cut_tool(frac_bar, 5, 6)
