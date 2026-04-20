extends SequenceEvent

func trigger() -> void:
	for interval in get_num_line_intervals():
		if interval.is_shaded:
			use_label_fraction_tool(interval, true)
