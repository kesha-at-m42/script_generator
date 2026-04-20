extends SequenceEvent

func trigger() -> void:
	use_highlight_tool(get_frac_shape_part(0,0), true)
	use_write_tool(get_frac_shape_part(0, 0), "1")
	await delay(.6)
	use_highlight_tool(get_frac_shape_part(0,1), true)
	use_write_tool(get_frac_shape_part(0, 1), "2")
	await delay(.6)
	use_highlight_tool(get_frac_shape_part(0,2), true)
	use_write_tool(get_frac_shape_part(0, 2), "3")
	await delay(.6)
	use_highlight_tool(get_frac_shape_part(0,3), true)
	use_write_tool(get_frac_shape_part(0, 3), "4")
