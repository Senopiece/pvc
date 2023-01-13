from pathlib import Path
import ffmpeg


def ffmpeg_compress(ifile: Path, ofile: Path) -> None:
    """Compresses a video using ffmpeg.
    Note that this removes audio at all.

    Args:
        ifile (Path): input video file
        ofile (Path): output video file
    """
    # video duration, in s
    duration = float(ffmpeg.probe(ifile)["format"]["duration"])

    # in bps
    target_total_bitrate = (1024 * 1024 * 8) / (1.07 * duration)

    # write output file
    ffmpeg.output(
        ffmpeg.input(ifile),
        **{
            "filename": ofile.absolute(),
            "c:v": "libx264",
            "b:v": target_total_bitrate,
        }
    ).overwrite_output().run()
