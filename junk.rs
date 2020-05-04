impl ToString for SectionStyle {
    fn to_string(&self) -> String {
        match self {
            SectionStyle::Box => "box".to_string(),
            SectionStyle::Plain => "plain".to_string(),
            SectionStyle::Underline => "underline".to_string(),
        }
    }
}



    let (head, tail) = it_1.first();
    for it in interleavings(it1.tail(), it2) {
        all = chain(all, [chain([first_1], it)]);
    }
    let first_2 = it_2.first();
    for it in interleavings(it1, it2.tail()) {
        all = chain(all, [chain([first_2], it)]);
    }

