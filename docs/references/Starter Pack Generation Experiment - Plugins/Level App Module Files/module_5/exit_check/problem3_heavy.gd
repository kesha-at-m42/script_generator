extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	clear_number_line_shaded_ticks(number_line)
	number_line.arrow_added.emit(0,6)
	await delay(1.5)
	number_line._ticks[6].numerator = 6
	number_line._ticks[6].denominator = 6
	use_label_fraction_tool(number_line._ticks[6], true)
	use_paint_tool(number_line._ticks[6])
