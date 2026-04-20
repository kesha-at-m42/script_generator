extends SequenceEvent

func trigger():
	insert_hint(get_num_line(), 1, 2)
