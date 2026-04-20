extends SequenceEvent

func trigger() -> void:
	reset_cuts(get_frac_shape())
	await delay(1)
	use_cut_tool(get_frac_shape(), 1, 2)
