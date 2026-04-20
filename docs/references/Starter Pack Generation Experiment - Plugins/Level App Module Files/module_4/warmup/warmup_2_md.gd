extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	var line = get_number_line()
	use_highlight_tool(bar._parts[0], true)
	use_cut_hint_tool(line.bar, 1, 4)
