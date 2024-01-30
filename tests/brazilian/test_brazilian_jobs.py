from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"

    result = read_brazilian_file(path)

    assert isinstance(result, list)

    assert len(result) > 0

    for job in result:
        assert "title" in job
        assert "salary" in job
        assert "type" in job

        assert "titulo" not in job
        assert "salario" not in job
        assert "tipo" not in job
