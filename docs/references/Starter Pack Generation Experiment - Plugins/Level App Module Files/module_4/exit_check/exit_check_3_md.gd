extends SequenceEvent

func trigger() -> void:
	use_highlight_tool(get_num_line_tick(0,1,2)._sum)
