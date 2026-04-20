extends SequenceEvent

func trigger():
	clear_number_line_ticks(get_num_line())
	use_cut_hint_tool(get_num_line(), 2, 4)
	use_cut_hint_tool(get_num_line(), 1, 4)
	use_cut_hint_tool(get_num_line(), 3, 4)