from matchzoo.preprocessor.arci_preprocessor import ArcIPreprocessor
import pytest

@pytest.fixture
def train_inputs():
    return [ ("id0", "id1", "beijing", "Beijing is capital of China", 1),
             ("id0", "id2", "beijing", "China is in east Asia", 0),
             ("id0", "id3", "beijing", "Summer in Beijing is hot.", 1)
           ]

@pytest.fixture
def validation_inputs():
    return [ ("id0", "id4", "beijing", "I visted beijing yesterday.") ]

def test_arci_preprocessor_noembed(train_inputs, validation_inputs):
    arci_preprocessor = ArcIPreprocessor()
    rv_train = arci_preprocessor.fit_transform(
        train_inputs,
        stage='train')
    assert len(rv_train.left) == 1
    assert len(rv_train.right) == 3
    assert len(rv_train.relation) == 3
    assert sorted(arci_preprocessor._context.keys()) == ['term_index']
    rv_valid = arci_preprocessor.fit_transform(
        validation_inputs,
        stage='test')
    assert len(rv_valid.left) == 1
    assert len(rv_valid.right) == 1
    assert len(rv_valid.relation) == 1

def test_arci_preprocessor_embed(train_inputs, validation_inputs):
    arci_preprocessor = ArcIPreprocessor("tests/sample/embed_word.txt")
    rv_train = arci_preprocessor.fit_transform(
        train_inputs,
        stage='train')
    assert len(rv_train.left) == 1
    assert len(rv_train.right) == 3
    assert len(rv_train.relation) == 3
    assert sorted(arci_preprocessor._context.keys()) == ['embedding_mat', 
                                                         'term_index']
    rv_valid = arci_preprocessor.fit_transform(
        validation_inputs,
        stage='test')
    assert len(rv_valid.left) == 1
    assert len(rv_valid.right) == 1
    assert len(rv_valid.relation) == 1
