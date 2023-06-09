fn log(msg: &str) {
    use std::fs::OpenOptions;

    let mut file = OpenOptions::new()
    .append(true)
    .create(true)
    .open("/tmp/log.txt")
    .unwrap();
    file.write(msg.as_bytes()).unwrap();
}
