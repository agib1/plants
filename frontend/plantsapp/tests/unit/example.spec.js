import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import HelloWorld from '@/views/Tests.vue'

describe('Tests.vue', () => {
  it('renders props.msg when passed', () => {
    const wrapper = mount(Tests)
    expect(wrapper.exists()).toBe(true)
  })
})
