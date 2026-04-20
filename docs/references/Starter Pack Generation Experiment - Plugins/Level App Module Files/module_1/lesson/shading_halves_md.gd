extends SequenceEvent

func trigger() -> void:
	use_paint_tool(get_frac_shape_part(0,0))
	use_paint_tool(get_frac_shape_part(0,1))
	use_highlight_tool(get_frac_shape_part(0,0), true)
