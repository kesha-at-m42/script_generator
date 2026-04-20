extends SequenceEvent

func trigger() -> void:
	await delay(.5)
	use_highlight_tool(get_frac_shape_part(0,0))
	await delay(1.75)
	clear_highlights(get_frac_shape())
	use_comp_frame_tool(get_frac_shape_part(), get_frac_shape_part(1))
