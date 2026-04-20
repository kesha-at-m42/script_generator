extends SequenceEvent

func trigger() -> void:
	var frac_bar := get_frac_shape(2)
	reset_cuts(frac_bar)
	await delay(1)
	use_cut_hint_tool(frac_bar, 4, 8)
	await delay(1)
	use_cut_hint_tool(frac_bar, 2, 8)
	await delay(1)
	use_cut_hint_tool(frac_bar, 6, 8)
	await delay(1)
	use_cut_hint_tool(frac_bar, 1, 8)
	await delay(1)
	use_cut_hint_tool(frac_bar, 3, 8)
	await delay(1)
	use_cut_hint_tool(frac_bar, 5, 8)
	await delay(1)
	use_cut_hint_tool(frac_bar, 7, 8)
