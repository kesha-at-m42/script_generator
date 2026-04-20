extends SequenceEvent

func trigger() -> void:
	clear_selected()
	use_select_tool(get_frac_shape())
	use_comp_frame_tool(get_frac_shape_part(), get_frac_shape_part(1))
