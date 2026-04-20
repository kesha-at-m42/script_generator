extends SequenceEvent

func trigger() -> void:
	var bar := get_frac_shape()

	clear_highlights(bar)
	clear_labels(bar)

	use_label_fraction_tool(bar._parts[0], true)
	use_select_tool(bar)
