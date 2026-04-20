extends SequenceEvent

func trigger() -> void:
	var bars = get_frac_shapes()
	clear_selected()
	use_label_fraction_tool(bars[0]._parts[0], true)
	use_label_fraction_tool(bars[1]._parts[0], true)
	use_select_tool(bars[0])
	use_select_tool(bars[1])
