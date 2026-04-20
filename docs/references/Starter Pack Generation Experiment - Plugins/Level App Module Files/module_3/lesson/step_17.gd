extends SequenceEvent

func trigger():
	for part in get_frac_shape()._parts:
		if part.is_shaded:
			part.is_read_only = true
