extends SequenceEvent

func trigger() -> void:
	clear_selected()
	use_write_tool(get_frac_shape_part(0,0), "1")
