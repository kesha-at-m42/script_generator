extends SequenceEvent

func trigger() -> void:
	var frac_bar := get_frac_shape()
	clear_highlights(frac_bar)
	use_highlight_tool(frac_bar._parts[0], true)
