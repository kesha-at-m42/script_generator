extends SequenceEvent

func trigger():
	var number_line = get_number_line(1)
	clear_number_line_shaded_ticks(number_line)
	number_line.arrow_added.emit(0,1)
	await delay(1.5)
	number_line.arrow_extended.emit(0,2)
	await delay(1.5)
	number_line.arrow_extended.emit(0,3)
	await delay(1.5)
	number_line.arrow_extended.emit(0,4)
