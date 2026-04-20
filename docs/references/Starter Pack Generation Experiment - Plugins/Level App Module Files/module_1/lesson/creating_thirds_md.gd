extends SequenceEvent

func trigger() -> void:
	use_cut_hint_tool(get_frac_shape(), 1, 3)
	await delay(.8)
	use_cut_hint_tool(get_frac_shape(), 2, 3)
