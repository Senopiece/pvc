from pathlib import Path
import ffmpeg


def ffmpeg_compress(ifile: Path, ofile: Path) -> None:
    """Compresses a video using ffmpeg.
    Note that this removes audio at all.

    Args:
        ifile (Path): input video file
        ofile (Path): output video file
    """
    # Video duration, in s.
    duration = float(ffmpeg.probe(ifile)["format"]["duration"])

    # Target total bitrate, in bps.
    target_total_bitrate = (1024 * 1024 * 8) / (1.07 * duration)

    audio_bitrate = 32000
    video_bitrate = target_total_bitrate - audio_bitrate

    ffmpeg.output(
        ffmpeg.input(ifile),
        **{
            "filename": ofile.absolute(),
            "c:v": "libx264",
            "b:v": video_bitrate,
            "pass": 1,
        }
    ).overwrite_output().run()
