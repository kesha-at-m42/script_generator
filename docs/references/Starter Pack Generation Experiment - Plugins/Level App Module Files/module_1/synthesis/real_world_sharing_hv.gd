extends SequenceEvent

func trigger() -> void:
	var bars = get_frac_shapes()
	clear_selected()
	use_select_tool(get_frac_shape())
