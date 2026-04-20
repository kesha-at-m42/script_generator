extends SequenceEvent

func trigger() -> void:
	use_label_fraction_tool(get_frac_shape_part(0, 0))
	use_label_fraction_tool(get_frac_shape_part(1, 0))
	use_label_fraction_tool(get_frac_shape_part(2, 0))
