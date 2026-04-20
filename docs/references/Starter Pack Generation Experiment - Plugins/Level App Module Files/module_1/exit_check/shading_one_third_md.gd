extends SequenceEvent

func trigger() -> void:
	clear_shaded(get_frac_shape())
	use_highlight_tool(get_frac_shape_part(0,0), true)
	await delay(1)
	use_highlight_tool(get_frac_shape_part(0,0), false)
	use_highlight_tool(get_frac_shape_part(0,1), true)
	await delay(1)
	use_highlight_tool(get_frac_shape_part(0,1), false)
	use_highlight_tool(get_frac_shape_part(0,2), true)
	await delay(1)
	use_highlight_tool(get_frac_shape_part(0,2), false)
