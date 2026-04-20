extends SequenceEvent

func trigger() -> void:
	await delay(0.75)
	use_cut_tool(get_frac_shape(), 1, 2)
