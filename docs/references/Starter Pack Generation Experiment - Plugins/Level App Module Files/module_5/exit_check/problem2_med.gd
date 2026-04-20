extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	clear_number_line_shaded_ticks(number_line)
	number_line.arrow_added.emit(0,8)
	await delay(0.25)
	for i in range(1,7):
		use_label_fraction_tool(number_line._ticks[i])
		await delay(0.25)
		use_label_fraction_tool(number_line._ticks[i], false)
