extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	for part in bar._parts:
		if part.is_shaded:
			use_label_fraction_tool(part, true)
