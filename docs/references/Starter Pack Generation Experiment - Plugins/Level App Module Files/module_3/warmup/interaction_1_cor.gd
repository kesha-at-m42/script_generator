extends SequenceEvent

func trigger() -> void:
	use_label_fraction_tool(get_frac_shape()._parts[0], true)
