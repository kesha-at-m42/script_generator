extends SequenceEvent

func trigger():
	use_update_fraction_tool(get_num_line_tick(0,1,4),5,0)
	use_write_tool(get_num_line_tick(0,2,4),"5")
	use_write_tool(get_num_line_tick(0,3,4),"5")
	use_write_tool(get_num_line_tick(0,4,4),"5")
