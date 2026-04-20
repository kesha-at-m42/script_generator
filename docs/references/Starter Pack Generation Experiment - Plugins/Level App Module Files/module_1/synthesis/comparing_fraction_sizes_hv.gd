extends SequenceEvent

func trigger() -> void:
	clear_selected()
	use_select_tool(get_frac_shape())
