// function for Mock API
const sleep = m => new Promise(r => setTimeout(r, m))
const menus = [
  {
    cName: 'Путешествия',
    cSlug: 'trips',
    cImage: 'https://source.unsplash.com/300x300/?cat,cats'
  },
  {
    cName: 'Блог',
    cSlug: 'blog',
    cImage: 'https://source.unsplash.com/300x300/?dog,dogs'
  },
  {
    cName: 'О нас',
    cSlug: 'about',
    cImage: 'https://source.unsplash.com/300x300/?wolf'
  },

]

export const state = () => ({
  categoriesList: []
})
export const mutations = {
  SET_MENU_LIST (state, menus) {
    state.menusList = menus
  }
}
export const actions = {
  async getMenusList ({ commit }) {
    try {
      await sleep(1000)
      await commit('SET_MENU_LIST', menus)
    } catch (err) {
      console.log(err)
      throw new Error('Внутреняя ошибка сервера, сообщите администратору')
    }
  }
}
