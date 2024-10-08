from basyx.aas import model

# Define semanticIDs
semantic_reference_1 = model.ExternalReference(
    (model.Key(
        type_=model.KeyTypes.GLOBAL_REFERENCE,
        value='https://iat.rwth-aachen.de/aas-repository-semantic-matcher/semanticIDs/1'
    ),)
)
semantic_reference_2 = model.ExternalReference(
    (model.Key(
        type_=model.KeyTypes.GLOBAL_REFERENCE,
        value='https://iat.rwth-aachen.de/aas-repository-semantic-matcher/semanticIDs/2'
    ),)
)

# Define Submodels
example_property_1 = model.Property(
    id_short='ExampleProperty',  # Identifying string of the element within the Submodel namespace
    value_type=model.datatypes.String,  # Data type of the value
    value='exampleValue',  # Value of the Property
    semantic_id=semantic_reference_1  # set the semantic reference
)
example_submodel_1 = model.Submodel(
    id_="https://iat.rwth-aachen.de/aas-repository-semantic-matcher/example_submodel_1",
    id_short="exampleSubmodel1"
)
example_submodel_1.submodel_element.add(example_property_1)

example_property_2 = model.Property(
    id_short='ExampleProperty2',  # Identifying string of the element within the Submodel namespace
    value_type=model.datatypes.String,  # Data type of the value
    value='exampleValue2',  # Value of the Property
    semantic_id=semantic_reference_1  # set the semantic reference
)
example_property_3 = model.Property(
    id_short='ExampleProperty3',  # Identifying string of the element within the Submodel namespace
    value_type=model.datatypes.String,  # Data type of the value
    value='exampleValue3',  # Value of the Property
    semantic_id=semantic_reference_2  # set the semantic reference
)
example_submodel_2 = model.Submodel(
    id_="https://iat.rwth-aachen.de/aas-repository-semantic-matcher/example_submodel_2",
    id_short="exampleSubmodel2"
)
example_submodel_2.submodel_element.add(example_property_2)
example_submodel_2.submodel_element.add(example_property_3)


if __name__ == "__main__":
    from aas_python_http_client import (ApiClient,
                                        Configuration,
                                        SubmodelRepositoryAPIApi)

    configuration = Configuration()
    configuration.host = "http://localhost:8080/api/v3.0"

    api_client = ApiClient(configuration=configuration)

    submodelRepoClient = SubmodelRepositoryAPIApi(api_client=api_client)

    all_submodels = submodelRepoClient.get_all_submodels().result
    print(all_submodels)

    submodelRepoClient.post_submodel(example_submodel_1)
    submodelRepoClient.post_submodel(example_submodel_2)

    all_submodels = submodelRepoClient.get_all_submodels().result
    print(all_submodels)
