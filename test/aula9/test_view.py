
def test_status_code(response_aula9_view):
    assert response_aula9_view.status_code == 200


def test_template(response_aula9_view):
    template_names = [template.name for template in response_aula9_view.templates]
    assert "aula9/aula9.html" in template_names
    assert "base.html" in template_names
    