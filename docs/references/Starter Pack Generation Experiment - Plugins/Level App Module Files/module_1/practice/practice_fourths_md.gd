extends SequenceEvent

func trigger() -> void:
	var frac_bar = get_frac_shape()
	use_cut_hint_tool(frac_bar, 1, 2)
	await delay(0.75)
	use_cut_hint_tool(frac_bar, 1, 4)
	await delay(0.75)
	use_cut_hint_tool(frac_bar, 3, 4)
