extends SequenceEvent

func trigger():
	clear_labels(get_frac_shape())
	for part in get_frac_shape()._parts:
		if part.is_shaded:
			part.is_read_only = true
