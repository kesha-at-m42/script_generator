extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	clear_number_line_shaded_ticks(number_line)
	number_line.arrow_added.emit(0,3)
	await delay(1.5)
	use_label_fraction_tool(number_line._ticks[3], true)
	use_choice_tool([1])
